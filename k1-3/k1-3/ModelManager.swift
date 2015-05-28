//
//  ModelManager.swift
//  k1-3
//
//  Created by 櫻木善将 on 2015/05/28.
//  Copyright (c) 2015年 YoshimasaSakuragi. All rights reserved.
//

import Foundation

class ModelManager{


    //-------------------------------
    // シングルトン
    //-------------------------------
    static let sharedInstance = ModelManager()
    private init() {}
    
    lazy var recommendModel = RecommendPageModel()
    
}