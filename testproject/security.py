USERS = {'admin':'password',
          'admin2':'123'}
GROUPS = {'admin':['group:editors'], 'admin2':['group:editors']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
