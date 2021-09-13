import requests
import threading,time


channels = []
zee_list = []

zeeresp = requests.get('https://catalogapi.zee5.com/v1/channel/bygenre?sort_by_field=channel_number&sort_order=ASC&genres=News&country=IN&translation=en&languages=en,hi,pa').json()

for chnl in zeeresp['items']:
    for gen in chnl['items']:
        zee_list.append(gen)

# def zee5(chn):
#     z_id = chn['id']
#     api_url = "https://wispy-mountain-0801.rds8896.workers.dev/?url={}".format(z_id)
#     z_json = requests.get(api_url).text
#     channel = {
#         'title': chn['title'],
#         'category': chn['genres'][0]['value'],
#         'language': chn['languages'][0],
#         'url': z_json}
#     channels.append(channel)


for chn in zee_list:
    #threading.Thread(target=zee5,args=(chnl,)).start()
    z_id = chn['id']
    api_url = "https://wispy-mountain-0801.rds8896.workers.dev/?url={}".format(z_id)
    z_json = requests.get(api_url).text
    channel = {
        'title': chn['title'],
        'category': chn['genres'][0]['value'],
        'language': chn['languages'][0],
        'url': z_json}
    channels.append(channel)

with open('Updated_Zee_channels.m3u', 'w') as f:
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
