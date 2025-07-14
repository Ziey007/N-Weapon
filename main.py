import wx
from gui.manager import GuiManager


class MyApp(wx.App):
    def OnInit(self) -> bool:
        """
        Purpose: App初始化
        """
        self.mananger = GuiManager(title="Manba 工具")
        self.frame = self.mananger.GetFrame(idx=0)
        self.frame.SetWindowStyleFlag(wx.STAY_ON_TOP )
        self.frame.Center()
        self.frame.Show(True)

        return True

    # end def

    def UpdateUI(self, idx: int = 0) -> None:
        """
        Purpose: 更新UI
        """
        self.frame.Show(False)
        self.frame = self.mananger.GetFrame(idx=idx)
        self.frame.Show(True)

    # end def


def main() -> None:
    """
    Purpose: 程序启动入口
    """
    app = MyApp()
    app.MainLoop()


# end def

if __name__ == "__main__":
    main()
# end main
