# Python code to take in JSON, and output a CSV file
# Format of JSON:
# "ts", "username", "platform", "ms_played", "conn_country", "ip_addr_decrypted", "user_agent_decrypted", "master_metadata_track_name", "master_metadata_album_artist_name", "master_metadata_album_album_name", "spotify_track_uri", "episode_name", "episode_show_name", "spotify_episode_uri", "reason_start", "reason_end", "shuffle", "skipped", "offline", "offline_timestamp", "incognito_mode"
import json
import csv
import sys

# Read in the JSON file
# This is the file that is passed in as an argument
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    data = json.load(f)

# Open the CSV file
# This is the file that is passed in as an argument
    
with open(sys.argv[2], 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Write the header
    writer.writerow(["ts","username","platform","ms_played","conn_country","ip_addr_decrypted","user_agent_decrypted","master_metadata_track_name","master_metadata_album_artist_name","master_metadata_album_album_name","spotify_track_uri","episode_name","episode_show_name","spotify_episode_uri","reason_start","reason_end","shuffle","skipped","offline","offline_timestamp","incognito_mode"])
    # Write the data
    for data in data:
        writer.writerow([data["ts"], data["username"], data["platform"], data["ms_played"], data["conn_country"], data["ip_addr_decrypted"], data["user_agent_decrypted"], data["master_metadata_track_name"], data["master_metadata_album_artist_name"], data["master_metadata_album_album_name"], data["spotify_track_uri"], data["episode_name"], data["episode_show_name"], data["spotify_episode_uri"], data["reason_start"], data["reason_end"], data["shuffle"], data["skipped"], data["offline"], data["offline_timestamp"], data["incognito_mode"]])
                        
# Print out the name of the file that was created
print("The file " + sys.argv[2] + " was created.")

# End of program