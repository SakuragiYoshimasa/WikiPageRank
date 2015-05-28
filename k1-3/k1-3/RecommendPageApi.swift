//
//  RecommendPageApi.swift
//  k1-3
//
//  Created by 櫻木善将 on 2015/05/28.
//  Copyright (c) 2015年 YoshimasaSakuragi. All rights reserved.
//

import Foundation
class RecommendPageApi:NSObject{
    
    static var manager:callback!
    var recommendTitle:NSString!

    static func getRecommendPage(url:NSURL,m:callback){
        
         manager = m
        
        //ここでクエリ投げて一番自作DBからtitleのlink先にある一番pagerankが高く関連性(Category)が近いものをリターン
        
        dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), {
            op().start()
        })
        
        

    }
    
    private static func recommend(){
        
        sleep(2)
        self.manager.fetchRecommendPageCallBack("織田信長")
    }
    
    class op:NSOperation {
        
        
        override init() {
            super.init()
            self.queuePriority = NSOperationQueuePriority.Normal
        }
        
        override func main() {
            
            //leep(2)
            //manager.fetchRecommendPageCallBack("織田信長")
            RecommendPageApi.recommend()
            
        }
    
    }
}