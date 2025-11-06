# # dictionaries
# from altair import value
#
# contact_info={
#     "Alice":"32423432",
#     "Bob":"534545345"
# }
#
# alice_phone=contact_info['Alice']
# print(alice_phone)
# contact_info['Daris']='045345454'
# print(contact_info)
# keys=contact_info.keys()
# print(keys)
# values=contact_info.values()
# print(values)
# items=contact_info.items()
# print(items)
# contact_info={
#     "Alice":{
#         "phone":"6784566",
#         "email":"alice@gmail.com"
#     }
# }
contact_info={
    "Alice":(
        "Alice":"676347589","alice@gmail.com"
    )
}
alice_info=contact_info['Alice']
phone=alice_info[0]

print(phone)
