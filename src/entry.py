from js import fetch, Response, console, JSON, Headers, FormData, File
import asyncio
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta


async def get_menu_data():
    # Fetch the RSS feed
    response = await fetch('https://www.stw-saarland.de/_menuAtom/1')
    text = await response.text()
    
    # Parse the XML content
    root = ET.fromstring(text)
    
    # Define namespaces to handle XML namespaces properly
    namespaces = {'atom': 'http://www.w3.org/2005/Atom'}
    
    # Get the current system date and calculate tomorrow's date
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_str = tomorrow.strftime("%d.%m.%Y")  # Format as dd.mm.yyyy
    
    # String to store only tomorrow's menu data
    tomorrow_menu_str = ""
    
    # Find all entries in the feed
    entries = root.findall('atom:entry', namespaces)
    
    for entry in entries:
        # Extract the title (date), link, and summary for each entry
        title = entry.find('atom:title', namespaces).text
        
        # Check if the date at the end of the title matches tomorrow's date
        # In the raw RSS, date are written in the title field
        if tomorrow_str in title:

            # Extract the summary filed
            summary = entry.find('atom:summary', namespaces).text
            # Store this entry's summary as menu string
            tomorrow_menu_str = summary
    return tomorrow_menu_str

async def assamble_openai_batch_request(menu_data, env):
    # Get api key from Secret
    api_key = env.API_KEY
    # Get prompts from KV. Languages are: en, fr, zh, kr, jp
    prompt_en = await env.menu_translation_kv.get("prompt_en")
    prompt_fr = await env.menu_translation_kv.get("prompt_fr")
    prompt_zh = await env.menu_translation_kv.get("prompt_zh")
    prompt_kr = await env.menu_translation_kv.get("prompt_kr")
    prompt_jp = await env.menu_translation_kv.get("prompt_jp")





async def on_fetch(request, env):

    # Get the menu data
    tomorrow_menu_str = await get_menu_data()
    

    # Print the menu data to console log
    # console.log(tomorrow_menu_str)
    console.debug(env.API_KEY)
    try:
        prompt = await env.menu_translation_kv.get("prompt_zh")
    except:
        console.debug("Error: prompt_zh not found")
    console.debug(prompt)
    
    # Return html response with the menu data as body
    return Response.new("", {
        "status": 200
    })
