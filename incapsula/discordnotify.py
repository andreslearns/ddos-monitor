#!/usr/bin/env python3
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File
 
# Create webhook

def imperva_notify(target, time):
    webhook = Webhook.partial("849854502517342258", "uuc_qbp1UwxsCx0LwYgI1TycOeuReT0-HLU6VNaXfUdrz7jIWgNy1cpPSvj0JgU03AuA",\
    adapter=RequestsWebhookAdapter())
    title =" ```ALERT! - DDOS DETECTED IN SPARC NETWORK INFRASTRUCTURE!```"
    # Send ddos text notification
    webhook.send(title)
    webhook.send(f"""```Target: {target}\nTime: {time}\n\n```""")
    webhook.send(f"""```#MANUAL DIVERT!#\nip access-list extended NORMAL\nno permit ip any any\ndeny ip {target} 0.0.0.255 any\npermit ip any any\n\nip access-list extended DIVERT\nno deny ip any any\npermit ip {target} 0.0.0.255 any\ndeny ip any any\ndo clear ip bgp * soft out\n```""")

# imperva_notify("113.61.58.0/24 40GB 40PPS")
# # Upload image to server
# webhook.send(file=discord.File(&quot;latest_img.jpg&quot;))