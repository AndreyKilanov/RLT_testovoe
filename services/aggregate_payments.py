from datetime import datetime as dt, timedelta
import calendar as clndr


def get_payments(
    db_data: list[dict], dt_from: dt, dt_upto: dt, group_type: str
):
    totals = {}

    match group_type:
        case 'hour':
            while dt_from <= dt_upto:
                totals[dt_from] = 0
                dt_from += timedelta(hours=1)
        case 'day':
            while dt_from <= dt_upto:
                totals[dt_from.date()] = 0
                dt_from += timedelta(days=1)
        case 'month':
            while dt_from <= dt_upto:
                totals[dt_from] = 0
                last_day = clndr.monthrange(dt_from.year, dt_from.month)[1]
                dt_from = dt_from.replace(day=last_day) + timedelta(days=1)

    for entry in db_data:
        date = None
        value = entry['value']

        match group_type:
            case 'hour':
                date = dt.fromisoformat(str(entry['dt']))
                date = date.replace(minute=0, second=0, microsecond=0)
            case 'day':
                date = dt.fromisoformat(str(entry['dt'])).date()
            case 'month':
                date = dt.fromisoformat(str(entry['dt']))
                date = dt(date.year, date.month, 1, 0, 0, 0)

        if date in totals:
            totals[date] += value
        else:
            totals[date] = value

    data_set = {
        "dataset": list(totals.values()),
        "labels": list(d.strftime('%Y-%m-%dT%H:%M:%S') for d in totals.keys()),
    }

    return data_set
