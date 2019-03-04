from Common.Basepage import Basepage

class Money(Basepage):

    money_id = 'id**com.sz.gcyh.KSHongBao:id/home_wallet_iv'  # 钱包
    back_id = 'id**com.sz.gcyh.KSHongBao:id/person_back_iv'  # 返回

    def money(self):
        self.find_element(self.money_id).click()
