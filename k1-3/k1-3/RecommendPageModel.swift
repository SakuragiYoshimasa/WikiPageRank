//
//  RecommendPageModel.swift
//  k1-3
//
//  Created by 櫻木善将 on 2015/05/28.
//  Copyright (c) 2015年 YoshimasaSakuragi. All rights reserved.
//

import Foundation

class RecommendPageModel:callback {
    
    //var api:RecommendPageApi!
    var observer:ViewController!
    
    init(){
        //api = RecommendPageApi()
    }
    
    func fetchRecommendPage(url:NSURL){
  
        RecommendPageApi.getRecommendPage(url, m: self)
    }
    
    
    func fetchRecommendPageCallBack(title:String) -> Void {
        if((observer != nil) && (title != "")){
            observer.observeFetchRecommendPage(title as String)
        }
    }
    
    func setObserver(vc:ViewController){
        self.observer = vc
    }
}