# -*- coding:utf-8 -*-
import sys
from selenium import  webdriver
reload(sys)
sys.setdefaultencoding( "utf-8" )
from selenium.webdriver.common.keys import Keys


class Yl_Web():
    u'''
    优啦Web测试库
    '''
    def __init__(self,driver):
        self.driver = eval('webdriver.%s()')%(driver)
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
    def By_id(self,id):
        try:return self.driver.find_element_by_id(id)
        except:raise Exception('No such element' )
    def By_xpath(self,xpath):
        try:return self.driver.find_element_by_xpath(xpath)
        except:raise Exception('No such element')
    def By_class_name(self,class_name):
        try:return self.driver.find_element_by_class_name(class_name)
        except:raise Exception('No such element')
    def By_link_text(self,link_test):
        try:return self.driver.find_element_by_link_text(link_test)
        except:raise Exception('No such element')
    def By_name(self,name):
        try:return self.driver.find_element_by_name(name)
        except:raise Exception('No such element')
    def By_partial_link_text(self,link_test):
        try:return self.driver.find_element_by_link_text(link_test)
        except:raise Exception('No such element')
    def By_tag_name(self,tagname):
        return self.driver.find_element_by_tag_name(tagname)
    def By_css_selector(self,css_selector):
        return self.driver.find_element_by_css_selector(css_selector)
    def By_ids(self,id):
        return self.driver.find_elements_by_id(id)
    def By_xpaths(self,xpath):
        return self.driver.find_elements_by_xpath(xpath)
    def By_class_names(self,class_name):
        return self.driver.find_elements_by_class_name(class_name)
    def By_link_texts(self,link_test):
        return self.driver.find_elements_by_link_text(link_test)
    def By_names(self,name):
        return self.driver.find_elements_by_name(name)
    def By_partial_link_texts(self,link_test):
        return self.driver.find_elements_by_link_text(link_test)
    def By_tag_names(self,tagname):
        return self.driver.find_elements_by_tag_name(tagname)
    def By_css_selectors(self,css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)
    def do(self,elements,todo,param=None):
        if param!=None:
            eval('elenments.' + todo + '(%s)'%(str(param)))
        eval(str(elements)+'.'+todo+'()')
    def get(self,elements,value):
        if value=='text':
            return eval('elements.text')
        if value=='title':
            return eval('elements.title')
        else:return  eval('elements.get_attribute(\'%s\')')
    def check(self,elenments,status):
        return eval('elements.%s()'%(status))



