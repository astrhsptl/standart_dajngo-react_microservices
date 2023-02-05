import React from 'react'
import { useLocation } from 'react-router-dom'
import Header from '../../UI/Header'

export default function RegisterPage() {
  return (
    <div className={'register-block'}>
    <Header path={useLocation().pathname}></Header>
      This is a register page
    </div>
  )
}
