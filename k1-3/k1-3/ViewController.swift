//
//  ViewController.swift
//  k1-3
//
//  Created by 櫻木善将 on 2015/05/27.
//  Copyright (c) 2015年 YoshimasaSakuragi. All rights reserved.
//

import UIKit

class ViewController: UIViewController,UIWebViewDelegate {
    
    var wikiView:UIWebView?
    
    var wikiURL = "http://ja.wikipedia.org/wiki/"
    
    var i = 0;

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.wikiView = UIWebView()
        self.wikiView?.frame = self.view.bounds
        self.wikiView?.delegate = self
        
        self.wikiView!.autoresizingMask = UIViewAutoresizing.FlexibleRightMargin |
            UIViewAutoresizing.FlexibleTopMargin |
            UIViewAutoresizing.FlexibleLeftMargin |
            UIViewAutoresizing.FlexibleBottomMargin |
            UIViewAutoresizing.FlexibleWidth |
            UIViewAutoresizing.FlexibleHeight
        
        self.view.addSubview(self.wikiView!)
        
  
        var url = NSURL(string: wikiURL)
        var request = NSURLRequest(URL: url!)
        
        self.wikiView?.loadRequest(request)
        
        ModelManager.sharedInstance.recommendModel.setObserver(self)
    }


    override func viewWillLayoutSubviews() {
        let statusBarHeight: CGFloat! = UIApplication.sharedApplication().statusBarFrame.height
        self.wikiView?.frame = CGRectMake(0, statusBarHeight, self.view.bounds.width, self.view.bounds.height)
    }
    
    func webViewDidFinishLoad(webView: UIWebView) {
         //画面遷移したらURLを取得
         if(webView.request?.URL != nil){
            i += 1
            //ごまかしてすみませんw
            if(i == 6 || i == 5 || i == 2 || i == 1){return}
            println(i)
            println(webView.request?.URL)
            ModelManager.sharedInstance.recommendModel.fetchRecommendPage(webView.request!.URL!)
            
        }
    }
    
    func observeFetchRecommendPage(keyword:String){
        
        let alert:UIAlertController = UIAlertController(title: "RecommnedPage!", message: keyword, preferredStyle: .Alert)
        
        let okAction = UIAlertAction(title: "OK", style: .Default) {action -> Void in
            self.i = 0
            var url = NSURL(string: self.wikiURL + keyword.stringByAddingPercentEscapesUsingEncoding(NSUTF8StringEncoding)!)
            var request = NSURLRequest(URL: url!)
            self.wikiView?.loadRequest(request)
            
        }
        let cancelAction = UIAlertAction(title: "CANCEL", style: .Cancel) {
            action in println("Pushed CANCEL")
        }
        
        alert.addAction(okAction)
        alert.addAction(cancelAction)
        
        presentViewController(alert, animated: true, completion: nil)
        

        
    }
}

