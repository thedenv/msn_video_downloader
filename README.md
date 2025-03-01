# msn_video_downloader
Python script that uses yt-dlp to download videos from MSN.com
First and foremost, you need Python (preferably the latest version) installed on your machine. 
Personally I installed it in the C:/ directory. 
You also need to install "requests" (the request module/Pythons package manager) 
after you install python open a command prompt and type:

$ pip install requests

Then verify that you have it by typing in command console:
$ python -c "import requests; print(requests.__version__)"

Once requests is installed, you can run the script:
python "C:\Users\*YOUR_USERNAME*\Desktop\Desktop Folders\youtube-dl\msn_video_downloader.py" "https://www.msn.com/en-gb/video/news/new-details-of-gene-hackman-and-wifes-death/vi-AA1A0qqW"

As you can see, I was so eager to get that video of Gene Hackman. For YOUR video, just replace the USERNAME with your own username and replace the video URL.

If you had success like I did, you will be prompted to choose a video format, or just press ENTER for best quality.

Example:
python "C:\Users\USERNAME\Desktop\Desktop Folders\youtube-dl\msn_video_downloader.py" "<your_url>"

Here is what the script did:
> Extracted Video Info: Parsed locale="en-gb" and page_id="AA1A0qqW" from the URL.
> Fetched JSON: Got the metadata from https://assets.msn.com/content/view/v2/Detail/en-gb/AA1A0qqW.
> Listed Qualities: Found six MP4 options:

[1001]: Highest quality (likely 1080p or source file).
[105]: ~6750 kbps (possibly 720p or 1080p lite).
[104]: ~3400 kbps.
[103]: ~2250 kbps.
[102]: ~1500 kbps.
[101]: ~650 kbps (lowest quality, maybe 360p or 480p).


Script created by the_denv on March 1st 2025
