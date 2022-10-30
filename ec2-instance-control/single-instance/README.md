# Single AWS EC2 instance controller using Discord Bot
This project is designed for small size of organization, by using this method can save server cost by detect and shutdown usused single instance. and this bot also support discord slash ```/``` commands!

## Required dependencies
- Python3, Python3-pip
- Discord library
- Py-cord library
- AWSCLI
- AWS Boto3

### by commands:
```
apt install python3 python3-pip -y
pip3 install awscli
pip3 install discord py-cord boto3
```
- To prevent AWSCLI installation error, use ```pip3 install awscli``` command alone first.

## Installation
1. Install required dependencies to the system
2. Set AWSCLI credentials to the system
3. Set EC2 instance ID in the code
4. Set Discord Bot credentials in the code
5. Save the bot file and make bot file executable
6. Try to run your bot
7. Make your bot run 24/7

### by commands:
```
apt install python3 python3-pip -y
pip3 install awscli
pip3 install discord py-cord boto3
aws configure # Make change AWS IAM credentials
vi bot.py # Make change instance-id and bot credentials
chmod u+x bot.py
./bot.py
screen -dmS bot python3 bot.py
```