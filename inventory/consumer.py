from main import redis, Product

key = 'order_completed'
group = 'inventory-group'

try:
    redis.xgroup_create(key, group)
except:
    print('Group already exist!')

    