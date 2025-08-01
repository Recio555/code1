# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:12:59 2024

@author: usuario
"""

while True:
 # Reset for the next round of tests
 candidate_found = False
 for mro_list in mro_lists:
 if not len(mro_list):
 # Any empty lists are of no use to the algorithm.
 continue
 # Get the first item as a potential candidate for the MRO.
 candidate = mro_list[0]
 if candidate_found:
 # Candidates promoted to the MRO are no longer of use.
 if candidate in mro:
 mro_list.pop(0)
 # Don't bother checking any more candidates if one was found.
 continue
 if candidate in itertools.chain(*(x[1:] for x in mro_lists)) :
 # The candidate was found in an invalid position, so we
 # move on to the next MRO list to get a new candidate.
 continue
 else:
 # The candidate is valid and should be promoted to the MRO.
 mro.append(candidate)
 mro_list.pop(0)
 candidate_found = True