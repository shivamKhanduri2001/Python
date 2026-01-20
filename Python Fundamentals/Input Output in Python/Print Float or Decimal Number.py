item=input("Please Enter the Item name: ")
order=input("Please Enter the amount: (e.g 12.4 kg)")
final_order=float(order.replace("kg", ""))
print("Your order for Item", item, "amount", final_order, "has confirmed")