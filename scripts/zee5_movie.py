import requests

channels = []

id = ['0-9-zeecinemahd',
      '0-9-tvpictureshd',
      '0-9-zeeanmolcinema',
      '0-9-zeeclassic',
      '0-9-zeecinema',
      '0-9-pictures',
      '0-9-zeeaction',
      '0-9-privéhd',
      '0-9-channel_2105335046',
      '0-9-209']

for i in id:
    api_url = "http://localhost:8080/playzee.php?c={}".format(i)

    #z_json = requests.get(api_url).text

    chnl_url = 'https://catalogapi.zee5.com/v1/channel/{}'.format(i)

    chn = requests.get(chnl_url).json()
    if "message" not in chn:
        channel = {
            'title': chn['title'],
            'category': chn['genres'][0]['value'],
            'language': chn['languages'][0],
            'url': api_url}
        channels.append(channel)

    
with open('./m3u/Zee5_Movie.m3u', 'w') as f:
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