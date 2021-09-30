'''애완동물을 소개해주세요'''
animal='강아지'
name='연탄'
age=4
hobby="산책"
is_adult=age>=3

#print("우리집 " + animal + "의 이름은 " + name + "이에요\n" + name + "의 나이는 " +  str(age) + "살 이고 " + hobby + "을 조아해요")
print("우리집",                            animal,"의 이름은",name ,"이에요\n",name,"의 나이는 ",age,"살 이고 ",hobby,"을 조아해요")
print(name + "는 어른일까요? " + str(is_adult))