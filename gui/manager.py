import wx
from gui.frame.index import IndexFrame


class GuiManager:
    
    def __init__(self, title: str = "",size: tuple=(1000,800),pos=(0,0), UpdateUI=None):
        """
        Purpose: 初始化
        """
        self.title = title
        self.size = size
        self.pos = pos
        self.UpdateUI = UpdateUI
        self.FrameDict = {}

    # end def

    def GetFrame(self, idx: int = 0) -> wx.Frame:
        """
        Purpose: 获取制定frame
        """
        frame = self.FrameDict.get(idx)
        if frame is None:
            # comment:
            frame = self._CreateFrame(idx)
            self.FrameDict[idx] = frame
        # end if
        return frame

    # end def

    def _CreateFrame(self, idx: int = 0):
        """
        Purpose: 创建制定frame
        """
        if (idx == 1):
            # comment: 
            frame = IndexFrame(parent=None,idx=idx,title=self.title,size=self.size,pos=self.pos,UpdateUI=self.UpdateUI)
        else:
            # comment: 默认界面
            frame = IndexFrame(parent=None,idx=idx,title=self.title,size=self.size,pos=self.pos,UpdateUI=self.UpdateUI)
        # end if
        return frame
    # end def
