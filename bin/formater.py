def format(data: dict):
    return (f"""
City: {data['location']['region']}

Weather in C: {data['current']['temp_c']}

Weather in F: {data['current']['temp_f']}

Wind speed in mph: {data['current']['wind_mph']}

Wind speed in kph: {data['current']['wind_kph']}

Description: {data['current']['condition']['text']}
""")