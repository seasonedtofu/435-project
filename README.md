# 435-project

CLI created using python.

To run the 435CLI.py, you must have paramiko installed. (pip install paramiko)

OPEN 435CLI.py with an editor and edit the ip/username/password for IBM cloud to your own username/pw.

The CLI is very crude and only has functions to return searches, CREATE, UPDATE, REMOVE functions not implemented to ensure database is not messed with.

To see ALL the CRUD functions/queries, look at queries.csv

---------------------------------------------------------------------------------------------------------------------------------------------------------

Returns groups by group name, format: "groups_name cycling"

Returns groups by interest, format: "groups_interest cycling"

Returns group members by group name, format: "group_members Cycling Noobs"

Returns events by location, format: "events_location CA"

Returns events by date range, format: "events_daterange 1/1/2020 1/15/2020"

Returns events by date, format: "events_date 1/1/2020"

Returns events by interest, format: "events_interest cycling"

Returns users by first or last name, format: "users_name andrew"

Returns users by username, format: "users_name USERNAME"

Returns group chat by group id, format: "chat_groupid 1"

Returns group chat by group name, format: "chat_groupname cycling noobs"

