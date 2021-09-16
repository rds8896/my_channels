import requests

channels = []

id = ['0-9-207',
      '0-9-348',
      '0-9-392',
      '0-9-393']

for i in id:
    api_url = "https://zee5-rds.herokuapp.com/?c={}".format(i)

    #z_json = requests.get(api_url).text

    chnl_url = 'https://catalogapi.zee5.com/v1/channel/{}'.format(i)

    chn = requests.get(chnl_url).json()
    channel = {
        'title': chn['title'],
        'category': chn['genres'][0]['value'],
        'language': chn['languages'][0],
        'url': api_url}
    channels.append(channel)


with open('./m3u/Zee5_Lifestyle.m3u', 'w') as f:
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