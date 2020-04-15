gen4id
======

Installation
>>>>>>>>>>>>>

Usage
>>>>>>>>

.. code-block::

    pip install gen4id


Normal
:::::::::

.. code-block::

    from gen4id import IncreaseGen
    ic = IncreaseGen(key_len=8)
    uid = ic.encode(increase_id=10)
    print(uid)


Use Random String
::::::::::::::::::
by default, it user the `gen4id.increase_gen.MIXED` as the random string for choose,  you can use a generate random string for you application

.. code-block::

    from gen4id import random_str,IncreaseGen
    from gen4id.increase_gen import MIXED

    rstr = random_str(MIXED)
    ic = IncreaseGen(choose=rstr,key_len=10)
    uid = ic.encode(increase_id=10)
    print(uid)


Add Digit Check Bit
::::::::::::::::::::

.. code-block::

    from gen4id import random_str,IncreaseGen
    from gen4id.increase_gen import MIXED

    rstr = random_str(MIXED)
    ic = IncreaseGen(choose=rstr,key_len=10,digit=True,digit_bit=2)
    uid = ic.encode(increase_id=10)
    print(uid)

More
>>>>>>>>>

To Be Continue ....






