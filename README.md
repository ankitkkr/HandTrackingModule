# HandTrackingModule

The module server 3 main perpus:
1. findhand
2. findpostion
3. fingersup

The above 3 are the realy functions of the module which can be used just by calling after import this module in any of you projects

The Findhand Function:
It takes the video captured as an input and plots the trackers over your hand, the user has the freedom to specify which hand to be tracked, the tracking pointers need to be drawn or not and more. It last the user can get the optimum tracked image as a return to be displayed on their own project.

The FindPosition Function:
It provide a list with the x,y coorinate of each and every tracked pointers of you hand, along with the x,y coordinte it consist of the id number also at its 1st elemet to justify teh coordinates, also the coordinates displayed are calculated over the dimension of your video capture, so it don't require and further calculation.

The FingerUp Function:
This function informs which of the fingures are out while tracking, and it returns a list of 5 where which ever finger is out it append 1 for it else 0, NOTE: The cases for left and right hand may differ, therfore its advices to specify the hand while calling the function where : Lefthand=0 & Righthand=1.
