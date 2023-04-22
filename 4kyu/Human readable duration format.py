def format_duration(seconds):
    result = ''
    # years
    if not seconds:
        return 'now'

    years = seconds // 31536000
    seconds -= (years * 31536000)
    if seconds == 0:
        if years == 1:
            return f'{years} year'
        else:
            return f'{years} years'
    else:
        if years > 0:
            if years == 1:
                result += f'{years} year, '
            else:
                result += f'{years} years, '

    # days
    days = seconds // 86400
    seconds -= (days * 86400)
    if seconds == 0:
        if result == '':
            if days == 1:
                result += f'{days} day'
                return result
            else:
                result += f'{days} days'
                return result
        else:
            if days == 1:
                result = result[:len(result) - 2] + ' '
                result += f'and {days} day'
                return result
            else:
                result = result[:len(result) - 2] + ' '
                result += f'and {days} days'
                return result
    else:
        if days > 0:
            if days == 1:
                result += f'{days} day, '
            else:
                result += f'{days} days, '
    # hour
    hours = seconds // 3600
    seconds -= (hours * 3600)
    if seconds == 0:
        if result == '':
            if hours == 1:
                result += f'{hours} hour'
                return result
            else:
                result += f'{hours} hours'
                return result
        else:
            if hours == 1:
                result = result[:len(result) - 2] + ' '
                result += f'and {hours} hour'
                return result
            else:
                result = result[:len(result) - 2] + ' '
                result += f'and {hours} hours'
                return result
    else:
        if hours > 0:
            if hours == 1:
                result += f'{hours} hour, '
            else:
                result += f'{hours} hours, '
    # minutes
    minutes = seconds // 60
    seconds -= (minutes * 60)
    if seconds == 0:
        if result == '':
            if minutes == 1:
                result += f'{minutes} minute'
                return result
            else:
                result += f'{minutes} minutes'
                return result
        else:
            if minutes == 1:
                result = result[:len(result) - 2] + ' '
                result += f'and {minutes} minute'
                return result
            else:
                result = result[:len(result) - 2] + ' '
                result += f'and {minutes} minutes'
                return result
    else:
        if minutes > 0:
            if minutes == 1:
                result += f'{minutes} minute, '
            else:
                result += f'{minutes} minutes, '
    # seconds
    seconds_new = seconds
    if seconds_new > 0 and result != '':
        if seconds_new == 1:
            result = result[:len(result) - 2] + ' '
            result += f'and {seconds_new} second'
        else:
            result = result[:len(result) - 2] + ' '
            result += f'and {seconds_new} seconds'
    else:
        if seconds_new == 1:
            return f'{seconds_new} second'
        else:
            return f'{seconds_new} seconds'

    return result


print(format_duration(3662))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(7582135))
print(format_duration(4951508))
print(format_duration(0))
print(format_duration(62))
print(format_duration(132030240))
print(format_duration(22))
