

def test_regist_clothes():
    myclothes=myclothes()

    clothes=Clothes()

    myclothes.regist_clothes(clothes)

    assert len(myclothes.clothes)== 1


def test_modify_clothes():
    
    pass


def test_remove_clothes():
    pass