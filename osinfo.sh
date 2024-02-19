#Preamble: Name and Identification
echo "Commencing XE103 Project: Linux Fundamental"
echo "Unit: CFC090423"
echo "Student Code: S10, Name: Fransiskus"
echo ""
sleep 4
echo "Initiating Task 1/5: Displaying Linux Version"
sleep $(($RANDOM%5))

#1. Display the Linux version. 
hostnamectl | grep Kernel | awk -F: '{print $NF}' | awk -F- '{print $1}' | tr -d [:blank:]

sleep $(($RANDOM%5))
echo "Task 1/5 Executed"
echo ""
echo "Initiating Task 2/5: Displaying IP Addresses"
sleep $(($RANDOM%5))

#2. Display the private IP address, public IP address, and the default gateway
#Private IP address
IPI=$(ifconfig | grep broadcast | awk '{print $2}')
echo "Your Private IP Address is: $IPI"

#Public IP address
IPE=$(curl -s ifconfig.io)
echo "Your Public IP Address is: $IPE"

#Default Gateway
DG=$(route | grep UG | awk '{print $2}')
echo "Your Default Gateway IP Address is: $DG"
sleep 4
 
echo "Task 2/5 Executed"
echo ""
echo "Initiating Task 3/5: Displaying Hard Disk Sizes"
sleep $(($RANDOM%5))

#3. Display the hard disk size; free and used space.
sleep $(($RANDOM%7))

# Used Space
USEDSPACE=$(df | awk '{total += $3} ; END {print total}')
# Free Space
FREESPACE=$(df | awk '{total += $4} ; END {print total}')

US=$(numfmt --grouping $USEDSPACE)
FS=$(numfmt --grouping $FREESPACE)

echo "The Hard Disk Size is: "
echo "Used Space: $US Kb"
echo "Free Space: $FS Kb" 

sleep 3

sleep $(($RANDOM%5)) 
echo "Task 3/5 Executed"
echo ""
echo "Initiating Task 4/5: Displaying Top 5 Directories"

sleep $(($RANDOM%5))

#4. Display the top five (5) directories and their size.
echo "The Top 5 Directories are:"
du -hs * | sort -rh | head -n 5

sleep 2
echo "Task 4/5 Executed"
sleep 5

#5. Display the CPU usage; refresh every 10 seconds.
while : ; 
do
clear
echo "Initiating Task 5/5: Displaying CPU Usage"
echo ""

cat /proc/stat|grep -w cpu|awk '{print ($5*100)/($2+$3+$4+$5+$6+$7+$8+$9+$10+$11)}'|awk '{print "CPU Usage: " 100-$1 "%"}'

echo ""
echo "Refreshing every 10 seconds"
echo ""
echo "Task 5/5 Executed"
echo "To terminate the process, please press [Ctrl + c]"
sleep 10
done



