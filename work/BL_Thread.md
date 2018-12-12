# 关于BL_Thread.h

```cpp
/**
 * @code
 * //declare the user thread class
 * class XXX_Thread : public BL_Thread
 * {
 *  public:
 *     XXX_Thread(){}
 *     virtual ~XXX_Thread(){}
 *
 *     virtual const TCHAR* GetThreadName();
 *
 *     virtual void Run();
 *
 *     //Start the Thread
 *     VOID XXX_Start()
 *     {
 *          BL_Thread::StartRegistThread();
 *     }
 *
 *     //Stop the Thread
 *     VOID XXX_Stop()
 *     {
 *          BL_Thread::StopThread();
 *     }
 *
 * };
 *
 * //implement the user thread class
 * const TCHAR*
 * XXX_Thread::GetThreadName()
 * {
 *     //return the registered Thread Name, please see AplThreadName.h
 *     return XXX_THREAD;
 * }
 *
 * void
 * XXX_Thread::Run()
 * {
 *    while(1){
 *        //check quit flag
 *        if(CheckQuit()) break;
 *
 *      //TODO: add user codes here!
 *      //call break; to quit thread
 *      //call Wait(msec); to sleep a while
 *      //call Wait(INFINITE); to wait for Notify()
 *  }
 *
 * }
 *
 * @endcode
 *
 */
```

## NOTE

* 当一个类集成`BL_Thread`时,在构造函数中需要调用`RegisterName(threadName.c_str());`

```cpp
VR_Recog::VR_Recog(const std::string &threadName)
{
    RegisterNamer(threadName.c_str());
    StartRegistThread(); // 顺便开始线程
}
```

* 开始之后就会调用子类重写的`Run()`方法.

```cpp
VOID VR_Recog::Run()
{
    while (true) {
        Wait(); // 线程开始时,调用了Run方法,在这里等待,知道Notify()方法调用.
        if (CheckQuit()) {
            break;
        }
        // TO DO
        // do something
    }
}
```

* 如果停止线程需要调用`StopThread()`即可

```cpp
VR_Recog::~VR_Recog()
{
    StopThread();
}
```