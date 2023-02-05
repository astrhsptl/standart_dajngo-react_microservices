import React from 'react'
import Header from '../../UI/Header'
import { useLocation } from 'react-router-dom'

export default function LoginPage() {
  return (
    <div className={'login-page'}>
        <Header path={useLocation().pathname}></Header>
        This is a login page
    </div>
  )
}
