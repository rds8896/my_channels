import requests

categories = ['News','Entertainment', 'Music', 'Movie', 'Lifestyle']

channels = []

mx_link = 'https://api.mxplay.com/v1/web/live/channels?device-density=2'
mx_json = requests.get(mx_link).json()

mx_channel_list = mx_json['channels']

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
                   ]

for i in mx_channel_list:

    lang = i['languages']


    if  (i['category'] == 'Music' or i['category'] == 'News' or i['category'] == 'Movies' or i['category'] == 'Lifestyle') and (lang[0]['name'] == 'Hindi' or lang[0]['name'] == 'English' or lang[0]['name'] == 'Punjabi' ):
        if i['category'] == 'Movies':
            mx_cat = 'Movie'
        else:
            mx_cat = i['category']
        if i['title'] in delete_channels:
            continue
        else:
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


with open('./m3u/mx_sony.m3u', 'w') as f:
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

    f.write('\n#EXTINF:-1 tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Sony_HD.png" group-title="Entertainment",SONY HD')
    f.write('\nhttps://pubads.g.doubleclick.net/ssai/event/HgaB-u6rSpGx3mo4Xu3sLw/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="" group-title="Punjabi",PTC Punjabi')
    f.write('\nhttps://streaming.ptcplay.com/ptcPunjabiINOne/smil:Live.smil/chunklist_w1389871650_b1396000_sleng.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="" group-title="Punjabi",PTC Punjabi Gold')
    f.write('\nhttps://streaming.ptcplay.com/ptcpunjabiGoldINOne/smil:Live.smil/chunklist_w1855918665_b1396000_sleng.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="" group-title="Punjabi",Punjabi Zindabad')
    f.write('\nhttp://stream.pztv.online/pztv/tracks-v1a1/mono.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Sony_SAB.png" group-title="Entertainment",SAB HD')
    f.write('\nhttps://pubads.g.doubleclick.net/ssai/event/UI4QFJ_uRk6aLxIcADqa_A/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Sony_Pal.png" group-title="Entertainment",SONY PAL')
    f.write('\nhttps://pubads.g.doubleclick.net/ssai/event/rPzF28qORbKZkhci_04fdQ/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Sony_Max_HD.png" group-title="Movie",SONY MAX HD')
    f.write('\nhttps://pubads.g.doubleclick.net/ssai/event/HgaB-u6rSpGx3mo4Xu3sLw/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/SET_MAX.png" group-title="Movie",SONY MAX')
    f.write('\nhttps://pubads.g.doubleclick.net/ssai/event/oJ-TGgVFSgSMBUoTkauvFQ/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Sony_Wah.png" group-title="Movie",SONY WAH')
    f.write('\nhttps://pubads.g.doubleclick.net/ssai/event/H_ZvXWqHRGKpHcdDE5RcDA/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Sony_MAX2.png" group-title="Movie",SONY MAX2')
    f.write('\nhttps://pubads.g.doubleclick.net/ssai/event/4Jcu195QTpCNBXGnpw2I6g/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Sony_Pix_HD.png" group-title="Movie",SONY PIX HD')
    f.write('\nhttps://pubads.g.doubleclick.net/ssai/event/8FR5Q-WfRWCkbMq_GxZ77w/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-id="144" tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Six_HD.png" group-title="Sports",SONY SIX HD')
    f.write('\nhttps://pubads.g.doubleclick.net:443/ssai/event/DD7fA-HgSUaLyZp9AjRYxQ/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-id="144" tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Ten_HD.png" group-title="Sports",SONY TEN 1 HD')
    f.write('\nhttps://pubads.g.doubleclick.net:443/ssai/event/yeYP86THQ4yl7US8Zx5eug/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-id="144" tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Ten2_HD.png" group-title="Sports",SONY TEN 2 HD')
    f.write('\nhttps://pubads.g.doubleclick.net:443/ssai/event/Syu8F41-R1y_JmQ7x0oNxQ/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-id="144" tvg-logo="http://jiotv.catchup.cdn.jio.com/dare_images/images/Ten3_HD.png" group-title="Sports",SONY TEN 3 HD')
    f.write('\nhttps://pubads.g.doubleclick.net:443/ssai/event/nmQFuHURTYGQBNdUG-2Qdw/master.m3u8')
    f.write('\n#EXTINF:-1 tvg-id="" tvg-name="STAR Sports 1 HD" tvg-logo="" group-title="Sports",STAR Sports 1 HD')
    f.write('\nhttp://echootv.tv:2086/sipantaroyan_FMUqUy/SdhIHYZ5Fz/241506')
    f.write('\n#EXTINF:-1 tvg-id="" tvg-name="STAR Sports 2 HD" tvg-logo="" group-title="Sports",STAR Sports 2 HD')
    f.write('\nhttp://echootv.tv:2086/sipantaroyan_FMUqUy/SdhIHYZ5Fz/241505')
    f.write('\n#EXTINF:-1 tvg-id="" tvg-name="STAR Sports Select 1 HD" tvg-logo="" group-title="Sports",STAR Sports Select 1 HD')
    f.write('\nhttp://echootv.tv:2086/sipantaroyan_FMUqUy/SdhIHYZ5Fz/241504')
    f.write('\n#EXTINF:-1 tvg-id="" tvg-name="STAR Sports Select 2 HD" tvg-logo="" group-title="Sports",STAR Sports Select 2 HD')
    f.write('\nhttp://echootv.tv:2086/sipantaroyan_FMUqUy/SdhIHYZ5Fz/241503')
    f.write('\n#EXTINF:-1 tvg-id="" tvg-name="DD Sports" tvg-logo="" group-title="Sports",DD Sports')
    f.write('\nhttp://echootv.tv:2086/sipantaroyan_FMUqUy/SdhIHYZ5Fz/241499')
    f.write('\n#EXTINF:-1 tvg-id="" tvg-name="Eurosport HD" tvg-logo="" group-title="Sports",Eurosport HD')
    f.write('\nhttp://echootv.tv:2086/sipantaroyan_FMUqUy/SdhIHYZ5Fz/241498')
    f.write('\n#EXTINF:-1 tvg-id="" tvg-name="Eurosport" tvg-logo="" group-title="Sports",Eurosport')
    f.write('\nhttp://echootv.tv:2086/sipantaroyan_FMUqUy/SdhIHYZ5Fz/241497')
    f.write('\n#EXTINF:-1 tvg-id="" tvg-name="1sports" tvg-logo="" group-title="Sports",1sports')
    f.write('\nhttp://echootv.tv:2086/sipantaroyan_FMUqUy/SdhIHYZ5Fz/241496')
