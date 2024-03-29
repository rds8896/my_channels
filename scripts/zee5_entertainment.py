import requests,time

channels = []

entertainment_id = ['0-9-bigmagic_1786965389',
                    '0-9-zeetvhd',
                    '0-9-tvhd_0',
                    '0-9-zeeanmol',
                    '0-9-215',
                    '0-9-165',
                    '0-9-zeetv',
                    '0-9-ddpunjabi',
                    '0-9-176',
                    '0-9-250']


for i in entertainment_id:
    api_url = "http://localhost:8080/playzee.php?c={}".format(i)

    #z_json = requests.get(api_url, timeout=(2,5)).status_code

    chnl_url = 'https://catalogapi.zee5.com/v1/channel/{}'.format(i)

    chn = requests.get(chnl_url).json()
    if "message" not in chn:
        channel = {
            'title': chn['title'],
            'category': chn['genres'][0]['value'],
            'language': chn['languages'][0],
            'url': api_url}
        channels.append(channel)


with open('./m3u/Zee5_Entertainment.m3u', 'w') as f:
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