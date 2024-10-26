MENU={
    "espresso":{
        "ingeridents":{
            "water":50,
            "coffee":18, 
            
        },
        "cost":1.5,
    },
    "latte":{
        "ingeridents":{
            "water":200,
            "milk":150,
            "coffee":24,

        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingeridents":{
            "water":250,
            "milk":100,
            "coffee":24,

        },
        "cost":3.0,
    }
}
profit=0
resource={
    "water":300,
    "milk":250,
    "coffee":100,
}
def  resource_is_sufficient(order_ingeridents):
    for item in order_ingeridents:
        if order_ingeridents[item]>resource[item]:
            print(f"sorry there is not enought{item}.")
            return False
    return True

def process_coin():
    print("please insert coin.")
    total=int(input("how many quarters:"))*0.25 
    total+=int(input("how many dimes:"))*0.1
    total+=int(input("how many nickeles:"))*0.05
    total+=int(input("how many penniess:"))*0.01
    return total

def transaction_is_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"here the ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry,that's not enough money. money refunded.")


def make_coffee(drink_name,order_ingeridents):
    for item in order_ingeridents:
        resource[item]-=order_ingeridents[item]
    print(f"here the {drink_name},ENJOY")
is_on=True

while is_on:
    choice=input("what would you like?(espresso/latte/cappuccino):")
    if choice=="off":
        is_on=False
    elif choice == "report":
        print(f"water:{resource['water']} ml")
        print(f"milk:{resource ['milk']}ml")
        print(f"coffee:{resource ['coffee']}g")
        print(f"cost:{profit}")
    else:
        drink=MENU[choice]
        if resource_is_sufficient(drink["ingeridents"]):
            payment=process_coin()
            if transaction_is_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingeridents"])


        