class Route:
    id = ''
    route_dict = {}
    """
    a = 0.0
    b = 0.0
    c = 0.0
    d = 0.0
    """ 
    def __init__(self, id, route_dict):
      self.id = id
      self.route_dict = route_dict
      """
      self.a = a
      self.b = b
      self.c = c
      self.d = d
      """
      

class Transition:
    id = ''
    #s01,s02,s13,s14,s15,s56,s26,s37,s48,s68, e = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
    trans_dict={}
    """def __init__(self, id, s01,s02,s13, s14,s15,s56,s26,s37,s48,s68,e):
      self.id = id
      self.s01, self.s02, self.s13, self.s14,self.s15,self.s56, self.s26, self.s37, self.s48,self.s68,self.e = s01,s02,s13, s14,s15,s56,s26,s37,s48,s68,e
    """
    def __init__(self,id, trans_dict):
        self.trans_dict = trans_dict
def route_init():
    route_list = []
    route_list.append(Route(id='s01', route_dict={'a':0.9,'b':0.1,'c':0.0,'d':0.0}))
    route_list.append(Route(id='s02',route_dict={'a':0.8,'b':0.0,'c':0.2,'d':0.0}))
    route_list.append(Route(id='s13',route_dict={'a':0.0,'b':1.0,'c':0.0,'d':0.0}))
    route_list.append(Route(id='s14',route_dict={'a':0.0,'b':1.0,'c':0.0,'d':0.0}))
    route_list.append(Route(id='s15',route_dict={'a':0.0,'b':0.6,'c':0.4,'d':0.0}))
    route_list.append(Route(id='s56',route_dict={'a':0.0,'b':0.2,'c':0.4,'d':0.4}))
    route_list.append(Route(id='s26',route_dict={'a':0.3,'b':0.0,'c':0.5,'d':0.2}))
    route_list.append(Route(id='s37',route_dict={'a':0.0,'b':0.2,'c':0.0,'d':0.8}))
    route_list.append(Route(id='s48',route_dict={'a':0.0,'b':0.2,'c':0.2,'d':0.6}))
    route_list.append(Route(id='s68',route_dict={'a':0.0,'b':0.0,'c':0.3,'d':0.7}))
    return route_list

def route_transition_init():
    route_transition = []
    route_transition.append(Transition('s',{'s01':0.1,'s02':0.1,'s13':0.1,'s14':0.1,'s15':0.1,'s56':0.1,'s26':0.1,'s37':0.1,'s48':0.1,'s68':0.1,'e':0.0}))
    route_transition.append(Transition('s01', {'s01': 0.0, 's02': 0.2, 's13': 0.2, 's14': 0.2, 's15': 0.2, 's56': 0.0,
                                             's26': 0.0, 's37': 0.0, 's48': 0.0, 's68': 0.0, 'e': 0.2}))
    route_transition.append(Transition('s02', {'s01': 0.33, 's02': 0.0, 's13': 0.0, 's14': 0.0, 's15': 0.0, 's56': 0.0,
                                               's26': 0.33, 's37': 0.0, 's48': 0.0, 's68': 0.0, 'e': 0.33}))
    route_transition.append(Transition('s13', {'s01': 0.2, 's02': 0.0, 's13': 0.0, 's14': 0.2, 's15': 0.2, 's56': 0.0,
                                               's26': 0.0, 's37': 0.2, 's48': 0.0, 's68': 0.0, 'e': 0.2}))
    route_transition.append(Transition('s14', {'s01': 0.2, 's02': 0.0, 's13': 0.2, 's14': 0.0, 's15': 0.2, 's56': 0.0,
                                               's26': 0.0, 's37': 0.0, 's48': 0.2, 's68': 0.0, 'e': 0.2}))
    route_transition.append(Transition('s15', {'s01': 0.2, 's02': 0.0, 's13': 0.2, 's14': 0.2, 's15': 0.0, 's56': 0.2,
                                               's26': 0.0, 's37': 0.0, 's48': 0.0, 's68': 0.0, 'e': 0.2}))
    route_transition.append(Transition('s56', {'s01': 0.0, 's02': 0.0, 's13': 0.0, 's14': 0.0, 's15': 0.25, 's56': 0.0,
                                               's26': 0.25, 's37': 0.0, 's48': 0.0, 's68': 0.25, 'e': 0.25}))
    route_transition.append(Transition('s26', {'s01': 0.0, 's02': 0.25, 's13': 0.0, 's14': 0.0, 's15': 0.0, 's56': 0.25,
                                               's26': 0.0, 's37': 0.0, 's48': 0.0, 's68': 0.25, 'e': 0.25}))
    route_transition.append(Transition('s37', {'s01': 0.0, 's02': 0.0, 's13': 0.5, 's14': 0.0, 's15': 0.0, 's56': 0.0,
                                               's26': 0.0, 's37': 0.0, 's48': 0.0, 's68': 0.0, 'e': 0.5}))
    route_transition.append(Transition('s48', {'s01': 0.0, 's02': 0.0, 's13': 0.0, 's14': 0.33, 's15': 0.0, 's56': 0.0,
                                               's26': 0.0, 's37': 0.0, 's48': 0.0, 's68': 0.33, 'e': 0.33}))
    route_transition.append(Transition('s68', {'s01': 0.0, 's02': 0.0, 's13': 0.0, 's14': 0.0, 's15': 0.0, 's56': 0.25,
                                               's26': 0.25, 's37': 0.0, 's48': 0.25, 's68': 0.0, 'e': 0.25}))
    """route_transition.append(Transition('s01',0.0, 0.2,0.2,0.2,0.2,0.0,0.0,0.0,0.0,0.0,0.2))
    route_transition.append(Transition('s02',0.33,0.0,0.0,0.0,0.0,0.0,0.33,0.0,0.0,0.0,0.33))
    route_transition.append(Transition('s13',0.2,0.0,0.0, 0.2, 0.2,0.0,0.0,0.2,0.0,0.0,0.2))
    route_transition.append(Transition('s14',0.2,0.0,0.2,0.0, 0.2,0.0,0.0,0.0, 0.2,0.0,0.2))
    route_transition.append(Transition('s15',0.2,0.0,0.2,0.2,0.0,0.2,0.0,0.0,0.0,0.0,0.2))
    route_transition.append(Transition('s56',0.0,0.0,0.0,0.0,0.25, 0.0,0.25,0.0,0.0, 0.25, 0.25))
    route_transition.append(Transition('s26',0.0,0.25,0.0,0.0,0.0,0.25,0.0,0.0,0.0,0.25,0.25))
    route_transition.append(Transition('s37',0.0,0.0,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.5))
    route_transition.append(Transition('s48',0.0,0.0,0.0,0.33,0.0,0.0,0.0,0.0,0.0, 0.33,0.33))
    route_transition.append(Transition('s68',0.0,0.0,0.0,0.0,0.0,0.25, 0.25,0.0, 0.25,0.0, 0.25))
    """

    return route_transition
def main():
    route_list = route_init()
    route_transition = route_transition_init()
    route_seq1= ['d','c','b','a']
    for node in route_seq1:
        for r in route_list:
            if(r.route_dict[node] is not 0.0):







if __name__=="__main__":
    main()

