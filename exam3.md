# 在multi-thread process中，若兩thread同時存取同一資料會發生甚麼問題?怎麼解決?
雖然在 multi-thread memory 可以共用，
但是如果兩個同時更改資料有可能會發生資料在還沒有被更新時，
就被另外一個 thread 取代了，
造成資料在存取時的錯誤


如果要解決這個問題就要使用 mutex lock，如果需要更新資料的時候，就將資料 lock 起來 避免跳到另外一個 thread 上更新資料