import wx

class IndexFrame(wx.Frame):
    def __init__(self,parent,idx,title,size,pos,UpdateUI=None):
        """
        Purpose: 
        """
        wx.Frame.__init__(self, parent, idx, title, size=size, pos=pos)
    # end def