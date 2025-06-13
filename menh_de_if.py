kpi = 100
result = 150
min_result = 50
base_salary = 1000

#result > kpi: luong = luong + luong * 0.2

if result > kpi:
   
#code block (phai hut dong vao trong)
#phep tinh luong
   base_salary = base_salary + base_salary * 0.2
print(base_salary)

if min_result > result:
   print("bn bi duoi:")

#result > min_result va ve hown kpi, canh bao

#toan tu logic

#and(phai thoa man tat ca dieu kien  cua toan tu)

#or(mot trong cac dieu kien duoc dap ung thi se chay code)

if result > min_result and result < kpi:
   print("ban can co gang hon")

