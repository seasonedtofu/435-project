# ----------------------------------------------------------------------------------------------------------------------
#
# Andrew Zhu
#
# ----------------------------------------------------------------------------------------------------------------------


# import 
from cmd import Cmd
import string
import paramiko as paramiko

hostname="12.42.205.8"
username="USERNAME"
password="PASSWORD"


class MyPrompt(Cmd):
    prompt = 'test>'
    intro = "Welcome! Type ? to list commands\n"

    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')



# -------------------------------------------------------------------------------------------------------------------
#
#  FUNCTIONS BEGIN HERE
#
# -------------------------------------------------------------------------------------------------------------------



    def do_groups_name(self,inp):
        '''Returns groups by group name, format: \"groups_name cycling\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select * from group_ where group_.name like \'%" + inp + "%\' ; \"")
        print (stdout.read())

    def do_groups_interest(self,inp):
        '''Returns groups by interest, format: \"groups_interest cycling\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select * from group_ where group_.interest like \'%" + inp + "%\' ; \"")
        print (stdout.read())
        
    def do_group_members(self,inp):
        '''Returns group members by group name, format: \"group_members Cycling Noobs\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select B.f_name,B.l_name,B.city,B.state,C.name,C.interest from user_group A LEFT JOIN user B on B.id=A.user_id LEFT JOIN group_ C on C.id=A.group_id where C.name like '%" + inp + "%' ; \"")
        print (stdout.read())

    def do_events_location(self,inp):
        '''Returns events by location, format: \"events_location CA\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select * from event where event.city like '%REPLACE%' OR event.state like '%" + inp + "%' ; \"")
        print (stdout.read())

    def do_events_daterange(self,inp):
        '''Returns events by date range, format: \"events_daterange 1/1/2020 1/15/2020\"'''
        x,y=inp.split()
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select * from event where date between '" + x + "' AND '" + y + "' ; \"")
        print (stdout.read())  

    def do_events_date(self,inp):
        '''Returns events by date, format: \"events_date 1/1/2020\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select * from event where date='" + inp + "' ; \"")
        print (stdout.read())  

    def do_events_interest(self,inp):
        '''Returns events by interest, format: \"events_interest cycling\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select A.date,A.name AS 'Event',B.interest,A.city,A.state,B.name AS 'Group' from event A LEFT JOIN group_ B on B.id=A.group_id WHERE B.interest LIKE '%" + inp + "%' ; \"")
        print (stdout.read())  

    def do_users_name(self,inp):
        '''Returns users by first or last name, format: \"users_name andrew\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select * from user where f_name LIKE '%" + inp + "%' or l_name LIKE '%" + inp + "%' ; \"")
        print (stdout.read())  

    def do_users_username(self,inp):
        '''Returns users by username, format: \"users_name USERNAME\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select * from user where username LIKE '%" + inp + "%' ; \"")
        print (stdout.read())  

    def do_chat_groupid(self,inp):
        '''Returns group chat by group id, format: \"chat_groupid 1\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select A.id, B.name, C.username, A.message from chat A LEFT JOIN group_ B on A.group_id=B.id LEFT JOIN user C on C.id=A.sender_id where A.group_id='" + inp + "'ORDER by A.id ASC ; \"")
        print (stdout.read())  

    def do_chat_groupname(self,inp):
        '''Returns group chat by group name, format: \"chat_groupname cycling noobs\"'''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
        client.connect(hostname, port=22, username=username, password=password)

        stdin, stdout, stderr = client.exec_command("mysql -u team07 -pTeamProject435! -D team07 -e \"select A.id, B.name, C.username, A.message from chat A LEFT JOIN group_ B on A.group_id=B.id LEFT JOIN user C on C.id=A.sender_id where B.name LIKE '%" + inp + "%' ORDER BY A.id ASC ; \"")
        print (stdout.read()) 


# -------------------------------------------------------------------------------------------------------------------
#
#  FUNCTIONS END HERE
#
# -------------------------------------------------------------------------------------------------------------------\


    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        print("Unrecognized Command: {}".format(inp))

    do_EOF = do_exit
    help_EOF = help_exit

if __name__ == '__main__':
    MyPrompt().cmdloop()

