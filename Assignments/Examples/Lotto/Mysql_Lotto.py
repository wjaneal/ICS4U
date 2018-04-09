import MySQLdb

conn = MySQLdb.connect (host = "localhost",
                           user = "root",
                           passwd = "***********",
                           db = "lotto")
Lottery = 0
while Lottery < 1 or Lottery > 2:
        Lottery = input("Please select a lottery: (1) - 649; (2) - Max")
if Lottery == 1:
        LotterySize = 6
else:
         LotterySize = 7

NewNumbers = [0]*(LotterySize+1)
if LotterySize == 6:
	LottoText = "lotto649"
	LottoFields = "(n1, n2, n3, n4, n5, n6, bonus, drawdate)"
if LotterySize == 7:
	LottoText = "lottomax"
	LottoFields = "(n1, n2, n3, n4, n5, n6, n7, bonus, drawdate)"


cursor = conn.cursor ()
done = 0
while done != 1:
	for i in range(0, LotterySize):
		NewNumbers[i] = input("Please enter number")
	NewNumbers[LotterySize] = input("Please enter the bonus number ")
	LottoValues = "("
	for i in range(0, LotterySize):
		LottoValues +=str(NewNumbers[i])
		LottoValues +=" ,"
	LottoValues += str(NewNumbers[LotterySize]) + ", CURDATE())"
	cursor.execute("""INSERT into %s %s VALUES %s""" % (LottoText, LottoFields, LottoValues))
	Answer = raw_input("Are you finished? (y/n)")
	if Answer in ["y", "yes", "Y", "Yes"]:
		done = 1


