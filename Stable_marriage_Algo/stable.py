
import collections

#The women that the men prefer
preferred_rankings_men = {
	'ryan': 	['lizzy', 'sarah', 'zoey', 'daniella'],
	'josh': 	['sarah', 'lizzy', 'daniella', 'zoey'],
	'blake': 	['sarah', 'daniella', 'zoey', 'lizzy'],
	'connor': 	['lizzy', 'sarah', 'zoey', 'daniella']
}

#The men that the women prefer
preferred_rankings_women = {
	'lizzy': 	['ryan', 'blake', 'josh', 'connor'],
	'sarah': 	['ryan', 'blake', 'connor', 'josh'],
	'zoey':  	['connor', 'josh', 'ryan', 'blake'],
	'daniella':	['ryan', 'josh', 'connor', 'blake']
}

#Keep track of the people that "may" end up together
tentative_engagements 	= []

#Men who still need to propose and get accepted successfully
free_men 				= []

def init_free_men():
	'''Initialize the arrays of women and men to represent
		that they're all initially free and not engaged'''
	for man in preferred_rankings_men.keys():
		free_men.append(man)

def begin_matching(man):
	'''Find the first free woman available to a man at
		any given time'''

	print(f"DEALING WITH {man}")
	for woman in preferred_rankings_men[man]:

		#Boolean for whether woman is taken or not
		taken_match = [couple for couple in tentative_engagements if woman in couple]

		if (len(taken_match) == 0):
			#tentatively engage the man and woman
			tentative_engagements.append([man, woman])
			free_men.remove(man)
			print('%s is no longer a free man and is now tentatively engaged to %s'%(man, woman))
			break

		elif (len(taken_match) > 0):
			print('%s is taken already..'%(woman))

			#Check ranking of the current dude and the ranking of the 'to-be' dude
			current_guy = preferred_rankings_women[woman].index(taken_match[0][0])
			potential_guy = preferred_rankings_women[woman].index(man)

			if (current_guy < potential_guy):
				print('She\'s satisfied with %s..'%(taken_match[0][0]))
			else:
				print('%s is better than %s'%(man, taken_match[0][0]))
				print('Making %s free again.. and tentatively engaging %s and %s'%(taken_match[0][0], man, woman))

				#The new guy is engaged
				free_men.remove(man)

				#The old guy is now single
				free_men.append(taken_match[0][0])

				#Update the fiance of the woman (tentatively)
				taken_match[0][0] = man
				break

def stable_matching():
	'''Matching algorithm until stable match terminates'''
	while (len(free_men) > 0):
		for man in free_men:
			begin_matching(man)


def main():
	init_free_men()
	print(free_men)
	stable_matching()
	print(tentative_engagements)

main()


#The women that men prefer.

# preferred_rankings_men = {
#
#     'ryan':['lizzy', 'sarah', 'zoey', 'daniella'],
#     'josh':['sarah', 'lizzy', 'daniella', 'zoey'],
#     'blake':['sarah', 'daniella', 'zoey', 'lizzy'],
#     'connor':['lizzy', 'sarah', 'zoey', 'daniella']
#
# }
#
# #The men that women prefer.
#
# preferred_rankings_men = {
#
#     'lizzy':['ryan', 'blake', 'josh', 'connor'],
#     'sarah':['ryan', 'blake', 'connor', 'josh'],
#     'zoey':['connor', 'josh', 'ryan', 'blake'],
#     'daniella':['ryan', 'josh', 'connor', 'blake']
#
# }
#
#
# #Keeps track of the people that 'may' end up together
#
# tentative_engagements = []
#
#
# #Men who still need to propose and get accepted to go to the dance
#
# free_men = []
#
# def init_free_men():
#     #Creates a list for men current free. and pushing it to free_men list.
#     for man in preferred_rankings_men.items():
#         free_men.append(man)
#
# def stable_matching():
#     #When the lenght of free_men is greater than 0.
#     #Begin Matching algorithm.This algorithm will continues loop to tell the free_men list that its empty.
#     #And if its not empty taken each of the man and run the func.
#     while(len(free_men) > 0):
#         for man in free_men:
#             begin_matching(man)
#
# def begin_matching(man):
#     print(f'DEALING WITH {man}')
#     #For each women that this man preffers, go ahead and get a boolean that if shes taken.
#     for women in preferred_rankings_men[man]:
#         # We will get a touple of the women and her assoiciated match, if it exits then it will be a touple of the man and woman in the tentative_engagements list.
#         # Otherwise it will return and empty list meaning she is single.
#         taken_match = [couple for couple in tentative_engagements if woman in couple]
#
#         if (len(taken_match == 0)):
#             tentative_engagements.append([man,woman])
#             free_men.remove(man)
#             print('%s is no longer a free man and is now tentatively connected to %s'%(man,woman))
#             break
#
#         elif(len(taken_match)>0):
#             print('%s is taken already..'%(woman))
#             #This mean is the current guy is = to the woman that his current enganged too
#             current_guy = preferred_rankings_women[women].index(taken_match[0][0])
#             potential_guy = preferred_rankings_women[women].index(man)
#
#             if (current_guy < potential_guy):
#                 print('She is satisfied %s..'%(taken_match[0][0]))
#             else:
#                 print('%s is better than %s' % (man, taken_match[0][0]))
#                 print('Making %s free again.. and then tentatively accepte dance between %s and %s'%(man,woman))
#
#                 #The new guy is now engaged
#                 free_men.append(man)
#
#                 #The old guy is now single again.
#                 free_men.append(taken_match[0][0])
#
#                 #update the students for the dance of the woman
#
#                 taken_match[0][0] = man
#                 break
#
# def main():
#     init_free_men()
#     stable_matching()
#
#     print('Complete list of dance and acceptance\n')
#     print(tentative_engagements)
#
# if __name__== "__main__":
#     main()
