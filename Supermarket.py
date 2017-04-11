#Supermarket program
#My shopping list
shopping_list = []


#Prexsisting Store Stock
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

#Prexsisting Store prices    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

#Add Product
#Make sure product is already exsting
def addProduct():
        newProduct = input('What new product would you like to add');
        stockAmount = input('How many of that product do you have');
        productPrice = input('How much does that product cost');
        stock[newProduct] = stockAmount;
        prices[newProduct] = productPrice;
        print ("Product added succesfully");
#possible bugs
def addStockToProduct():
    productName = input('What product do you want to add stock to?');
    addAmount = input('How much %ss do you wish to add?' % productName);
    stock[productName] += int(addAmount);
    print('Succesfully added {0} to {1}'.format(str(addAmount), productName))    

#Compute Bill
def compute_bill():
    isDone=False;
    while isDone==False:
        billProducts = input('Type the * key when you are done \n Enter the product:');
        if (billProducts not in stock and billProducts != '*'):
                print("Sorry product not available")
        elif (billProducts== '*'):
            print('The items being purchased are: %s' % shopping_list)
            break;
        else:
            shopping_list.append(billProducts)

    total=0;
    for item in shopping_list:
        if stock[item] > 0:
            total+=prices[item]
            stock[item]-=1;
    print ('The total amount is %s' % total);






print("********Welcome to the supermarket suite program*******");

isDone=False;

while isDone==False:
    userDes = input('Would you like to \n 1.Add product to stock \n 2.Add stock to product \n 3.Print Stock \n 4.Compute a bill \n 5.Exit');

    if userDes=='1':
       addProduct();
       
    if userDes=='2':
        addStockToProduct();
    
    
    if userDes=='3':
        print(stock);

    if userDes=='4':
        print (compute_bill());

    if userDes=='5':
        break;



