from js import fetch, Response
import asyncio
import xml.etree.ElementTree as ET
import json

async def on_fetch(request, env):
    # Fetch the RSS feed
    response = await fetch('https://www.stw-saarland.de/_menuAtom/1')
    text = await response.text()
    
    # Parse the XML content
    root = ET.fromstring(text)
    
    # Define namespaces to handle XML namespaces properly
    namespaces = {'atom': 'http://www.w3.org/2005/Atom'}
    
    # List to store menu data
    menu_data = []
    
    # Find all entries in the feed
    entries = root.findall('atom:entry', namespaces)
    
    for entry in entries:
        # Extract the title (date), link, and summary for each entry
        title = entry.find('atom:title', namespaces).text
        summary = entry.find('atom:summary', namespaces).text
        link = entry.find('atom:link', namespaces).attrib.get('href')
        updated = entry.find('atom:updated', namespaces).text
        
        # Store this entry's data in a dictionary
        menu_entry = {
            "date": title,
            "link": link,
            "updated": updated,
            "menu": summary
        }
        
        # Append this menu entry to the list
        menu_data.append(menu_entry)
    
    # Convert the list of menu data to JSON
    json_output = json.dumps(menu_data, indent=4, ensure_ascii=False)
    
    # Return the JSON response
    return Response.new(json_output, {
        "headers": {
            "Content-Type": "application/json"
        }
    })
