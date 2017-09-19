# This is my configure files of the test.
There are 10 testcases in Ceili's PPT, here are the configuration files of testcase 1.

![](https://ws2.sinaimg.cn/large/006tKfTcly1fjp3c20xdtj311w0sidjy.jpg)

I don not upload my Pcap (Wireshark) files because they exceed the maximum size limit. But you can download these files and run them directly on your virtual machine without changing anything. After you run the test you can get all data you want. What's more, the configuration of the remaining 9 tests are all similar, I think you can do that very quickly.
 
Take testcase 1 as an example, I want to explain something.

1. Queues work well in the test. The flows are very smooth and the throughputs can reach the rates we set, which is much better than the case with meters.
![](https://ws3.sinaimg.cn/large/006tKfTcly1fjp3ariyy4j31kw0u643m.jpg)
![](https://ws2.sinaimg.cn/large/006tKfTcly1fjp3li0a99j31kw0u0796.jpg)
![](https://ws4.sinaimg.cn/large/006tKfTcly1fjp3m8socnj31kw0qgq8d.jpg)

2. How to set a queue in a switch? If we want to add a queue in the switch S1 of which the rate is exactly 5.35 Mbps, we use the following command. 
![](https://ws1.sinaimg.cn/large/006tKfTcly1fjp3v5kb1bj315s036gn2.jpg)
I pull all the commands in the file "**QueueConfig.sh".

2. You need to set the flow table manually in the switches. I put all the commands in the file "**FlowTableConfig.sh". All flow entries in the switch S1 are as follows:
    ![](https://ws2.sinaimg.cn/large/006tKfTcly1fjp3sv2fqlj315a06u41y.jpg)

3. The functions of flow-entries are limited. Althought Mininet is the best network emulator, it does not support some complicated operations.


##Current problems:

1. I should have write a script that generate all the configuration files automatically. This is not a difficult work, but I am now in the hospital. I am really sorry about this.


2. I haven't completed the implementation of FDM in the new testbed. The code should be in the file "**.py". I referred to previous code. However, There are some problems about the previous implementation of FDM. It cannot computes the right results in these testcases, I think we need to modify the code. 

3. There are some bugs of Minints and MPTCP. Although We can solve them using some strange methods and they will not influence the results, Ceili and Jae may be confused about our operations. 

