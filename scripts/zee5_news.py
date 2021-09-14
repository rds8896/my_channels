import requests

channels = []

news_id = ['0-9-aajtak',
           '0-9-zeenews',
           '0-9-170',
           '0-9-zeehindustan',
           '0-9-zeepunjabharyanahima',
           '0-9-162',
           '0-9-282',
           '0-9-indiatoday',
           '0-9-206',
           '0-9-274']


for i in news_id:
    api_url = "https://wispy-mountain-0801.rds8896.workers.dev/?url={}".format(i)

    z_json = requests.get(api_url).text

    chnl_url = 'https://catalogapi.zee5.com/v1/channel/{}'.format(i)

    chn = requests.get(chnl_url).json()
    channel = {
        'title': chn['title'],
        'category': chn['genres'][0]['value'],
        'language': chn['languages'][0],
        'url': z_json}
    channels.append(channel)


with open('Zee5_news.m3u', 'w') as f:
    f.write('#EXTM3U url-tvg="http://botallen.live/epg.xml.gz"\n')
    for channel in channels:
        f.write('\n')
        if channel['language'] == 'pa':
            f.write('#EXTINF:-1, tvg-logo="" group-title="{}",{}\n'.format('Punjabi', channel['title']))
            f.write(str(channel['url']))
        elif channel['category'] == 'News':
            f.write('#EXTINF:-1, tvg-logo="" group-title="{}",{}\n'.format(channel['category'],channel['title']))
            f.write(str(channel['url']))
        elif channel['category'] == 'Entertainment':
            f.write('#EXTINF:-1, tvg-logo="" group-title="{}",{}\n'.format(channel['category'], channel['title']))
            f.write(str(channel['url']))
        elif channel['category'] == 'Music':
            f.write('#EXTINF:-1, tvg-logo="" group-title="{}",{}\n'.format(channel['category'], channel['title']))
            f.write(str(channel['url']))
        elif channel['category'] == 'Movie':
            f.write('#EXTINF:-1, tvg-logo="" group-title="{}",{}\n'.format(channel['category'], channel['title']))
            f.write(str(channel['url']))
        elif channel['category'] == 'Lifestyle':
            f.write('#EXTINF:-1, tvg-logo="" group-title="{}",{}\n'.format(channel['category'], channel['title']))
            f.write(str(channel['url']))