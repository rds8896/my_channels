import requests

categories = ['News','Entertainment', 'Music', 'Movie', 'Lifestyle']

channels = []

mx_link = 'https://api.mxplay.com/v1/web/live/channels?device-density=2'
mx_json = requests.get(mx_link).json()

mx_channel_list = mx_json['channels']

mx_final_list = []

delete_channels = ['NewsX',
                   'India News UP',
                   'Gulistan News',
                   'Loksabha TV',
                   'India News MP',
                   'News India 24X7',
                   'Janta TV',
                   'IBC24',
                   'Sahara Samay National',
                   'Sahara Samay UP Uttrakhand',
                   'Sahara Samay Rajasthan',
                   'Sahara Samay MP Chhattisgarh',
                   'Sadhna MP Chattisgarh',
                   'Sadhna Plus',
                   'First India News Rajasthan',
                   'K News India',
                   'Hindi Khabar',
                   'Surya Samachar',
                   'France 24',
                   'DW English',
                   'DW English HD',
                   'ABP Ganga',
                   'XZone',
                   'News 1 India',
                   'Navtej TV',
                   'National Voice',
                   'News Only',
                   'Bharat Samachar',
                   'HNN 24x7',
                   'Jan TV',
                   'News 36',
                   'Network 10 New',
                   'Sudarshan News',
                   'GBN24 News Channel',
                   'Prime News',
                   'TNI Awaaz',
                   'AB News',
                   'AB Star News',
                   'APN News',
                   'VIP News',
                   'Jantantra TV',
                   'PT News',
                   'Prime TV',
                   'Update India',
                   'News24 MP CG',
                   'News State Uttar Pradesh Uttrakhand',
                   'News State Madhya Pradesh Chhattisgarh',
                   'Surya Cinema',
                    'Samachar Today',
                    'Today24',
                    'Pulse 24 News',
                    'DPK News']

for i in mx_channel_list:
    lang = i['languages']
    if i['title'] not in delete_channels and (i['category'] == 'Music' or i['category'] == 'News' or i['category'] == 'Movies' or i['category'] == 'Lifestyle') and (lang[0]['name'] == 'Hindi' or lang[0]['name'] == 'English' or lang[0]['name'] == 'Punjabi' ):
        mx_final_list.append(i)

for i in mx_final_list:

    if i['category'] == 'Movies':
        mx_cat = 'Movie'
    else:
        mx_cat = i['category']
    channel = {
                    'title':  i['title'],
                    'category' :  mx_cat,
                    'language' : lang[0]['id'],
                    'url' : i['stream']['mxplay']['hls']['main'] }
    channels.append(channel)

#### youtube live tv

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            # if windows:
            #     print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
            #     return
            # os.system('wget {url} -O temp.txt')
            # response = ''.join(open('temp.txt').readlines())
            # if '.m3u8' not in response:
            #     print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    return link[start : end]


#open youtube file list
with open('youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        youtube_url = ''
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
        else:
            youtube_url = grab(line)

        if youtube_url != '':
            channel = {
                'title': ch_name,
                'category': grp_title,
                'language': tvg_id,
                'url': youtube_url}
            channels.append(channel)

## github


with open('mx_sony.m3u', 'w') as f:
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


