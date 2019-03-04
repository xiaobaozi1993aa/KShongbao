from Common.Basepage import Basepage

class Person(Basepage):
    user_id = 'id**com.sz.gcyh.KSHongBao:id/take_red_packet_user_iv'  # 个人
    back_id = 'id**com.sz.gcyh.KSHongBao:id/person_back_iv'  # 返回

    #个人用户
    def shouhongbao(self):
        self.find_element(self.user_id).click()
        self.find_element(self.back_id).click()