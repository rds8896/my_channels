

with open('../Zee_channel.m3u','w') as f:

    f.write('#EXTM3U url-tvg="http://botallen.live/epg.xml.gz"\n')

    with open('./m3u/Zee5_Entertainment.m3u') as file:
        for line in file:
            if 'EXTM3U' in line:
                continue
            else:
                f.write(line)

    with open('./m3u/Zee5_news.m3u') as file:
        for line in file:
            if 'EXTM3U' in line:
                continue
            else:
                f.write(line)
    with open('./m3u/Zee5_Lifestyle.m3u') as file:
        for line in file:
            if 'EXTM3U' in line:
                continue
            else:
                f.write(line)

    with open('./m3u/Zee5_Movie.m3u') as file:
        for line in file:
            if 'EXTM3U' in line:
                continue
            else:
                f.write(line)
    with open('./m3u/Zee5_Music.m3u') as file:
        for line in file:
            if 'EXTM3U' in line:
                continue
            else:
                f.write(line)

    with open('./m3u/mx_sony.m3u') as file:
        for line in file:
            if 'EXTM3U' in line:
                continue
            else:
                f.write(line)
