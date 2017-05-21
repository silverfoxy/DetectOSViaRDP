# DetectOSViaRDP
This set of scripts tries to automate the process of detecting OS version using RDP and image processing.

## Connecting Using RDP and Taking a Screenshot
This script is based on https://github.com/ztgrace/sticky_keys_hunter
### Requirements
apt-get install xdotool imagemagick rdesktop bc parallel

### Running the script
Run rdpss.sh iplist.txt
* **iplist.txt**: is a text file containing ip addresses (1 address per line)
* Customize **$LIMIT** variable in rdpss.sh (default: 2) for parallel sessions (Tested with $LIMIT=50, checks ~75 ips per minute)
## Detecting OS From Screenshots			
### Requirements
pip install opencv-python numpy
python DetectOS.py ./images/ ./marker-xp.jpg > iplistxp.txt
* **./images**: contains screenshots taken by rdpss.sh script
* **marker-xp.jpg**: is a part of windows XP login screen that's specific to this OS, if this image is found within the screenshot, then we conclude that the operating system was Windows XP.
* **iplistxp.txt**: contains list of IP Addresses that are Windows XP.
* By changing the marker image we can detect other operating systems. (XP and 2003 are currently tested and available within this repo)

# Manually Testing your setup
## Copy Detected Images to Another Directory To Visually Test
copyselected.sh iplistxp.txt images images-xp
* **iplistxt.txt**
* **images**
* **images-xp**

## Some Sample markers (XP, 2003)
* ![marker2003.jpg](https://github.com/silverfoxy/DetectOSViaRDP/blob/master/marker2003.jpg "marker2003.jpg")
* ![markerxp.jpg](https://github.com/silverfoxy/DetectOSViaRDP/blob/master/marker-xp.jpg "markerxp.jpg")

## Analysis (FalsePositive / FalseNegative)
Tested on a Dataset of 12000 IP Addresses / Screenshots
* **FP**: 0 %
* **FN**: 0.2 %
### Manual Verification
find ./images/ -maxdepth 1 | grep -vf iplistxp.txt > rest.txt

cat rest.txt | while read line; do cp "$line" ./rest; done

We take all the screenshots that are not classified by our script and copy them into **rest** directory, we then visually analyze any False Negatives.
