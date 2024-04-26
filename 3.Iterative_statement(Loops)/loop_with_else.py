# cart = [10,17,39,22,66,71]
# for item in cart:
#     if item>300:
#         print("Order cannot be processed!")
#         break
#     print(item)
# else:
#     print("Congrats! All Order processed succefully.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
cart = [10,17,39,400,66,71]
for item in cart:
    if item>300:
        print("Order cannot be processed!")
        break
    print(item)
else:
    print("Congrats! ALL Order processed succefully.")