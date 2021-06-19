#open input file to read input
input_file =open("input.txt","r")
#open output file to write output
output_file = open("output.txt","w+")
goodies={}
out_list=[]
#reading input file 
for a in input_file:
    toRead_index_price=a.index(":")
    print(a[toRead_index_price+1:].strip())
    print(a[:toRead_index_price])
    goodies[a[:toRead_index_price]]=a[toRead_index_price+1:].strip()
print(goodies) 
single_prices=list(goodies.values())

single_prices=[int(i)for i in single_prices]
#sorted list in decsending order to get prices to be distributed in order
single_prices.sort(reverse=True)
print(single_prices)
#taking inputs
num_of_employees=int(input("Enter number of employees: "))
leng_considered=(len(single_prices)-num_of_employees)

print(leng_considered)

#finding minimum difference between highest and lowest
for i in range(leng_considered):
    max_price=single_prices[i]
    min_price=single_prices[num_of_employees+i]
    if i == 0:
        diff=max_price-min_price
        idx_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        idx_choosen=i

choosen_prices=single_prices[idx_choosen:num_of_employees+idx_choosen]
#differnce between high and low price
diff=max(choosen_prices)-min(choosen_prices)
print("And the difference between the chosen goodie with highest price and the lowest price is",diff)

cnt=0
for key,value in goodies.items():
    single_prices[cnt]
    print(value)
    if int(value)in choosen_prices and cnt<num_of_employees:
        str1=key+": "+value
        #preparing  list for output
        out_list.append(str1)
        cnt+=1
        print(str1)
#writing to output file
output_file.write("Here the goodies that are selected for distribution are: ")

output_file.write("\n")

for i in out_list:
    output_file.write(i)
    output_file.write("\n")
output_file.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(diff))

input_file.close()
output_file.close()